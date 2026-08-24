import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

MODEL_PATH = "cifar10_cnn.pth"


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
        )
        self.fc_layers = nn.Sequential(
            nn.Linear(128 * 4 * 4, 256),
            nn.ReLU(),
            nn.Linear(256, 10),
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(-1, 128 * 4 * 4)
        x = self.fc_layers(x)
        return x


@st.cache_resource
def load_model():
    model = CNN()
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model


def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor()
    ])
    image = image.convert("RGB")
    return transform(image).unsqueeze(0)


st.set_page_config(page_title="CIFAR-10 Image Classifier", layout="centered")

st.title("CIFAR-10 Image Classifier")
st.write("Upload an image and the model will classify it into one of 10 categories.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "avif", "webp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    model = load_model()
    input_tensor = preprocess_image(image)

    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    predicted_class = CLASS_NAMES[predicted.item()]
    confidence_score = confidence.item() * 100

    st.subheader("Prediction")
    st.write(f"**Class:** {predicted_class}")
    st.write(f"**Confidence:** {confidence_score:.2f}%")

    st.subheader("All Probabilities")
    prob_dict = {CLASS_NAMES[i]: probabilities[0][i].item() * 100 for i in range(10)}
    st.bar_chart(prob_dict)
