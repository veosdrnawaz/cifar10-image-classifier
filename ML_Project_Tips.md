# ML Project — Important Tips & Best Practices

> Save this file. Har naye project se pehle padh lena.

---

## 1. Pehle Requirements Finalize Karo, Phir Code

AI ko seedha "code bana do" mat bolo. Pehle ye clear karo:
- Dataset
- Target
- UI
- Deployment
- Expected output

## 2. Training aur UI Preprocessing Same Honi Chahiye

Jo preprocessing training mein use hui, inference mein **exactly wahi** honi chahiye. Ye bahut important hai.

## 3. Sab Ek Folder Mein Rakho

- Model + code + requirements + README
- Sirf notebook par depend mat karo

## 4. Files Alag Rakhna

Har project mein `train.py`, `evaluate.py` aur `app.py` alag rakhna better hai. Isse baad mein model improve ya UI update karna easy hota hai.

## 5. Results Save Karo

- Accuracy
- Loss graphs
- Confusion matrix
- Model file

Teacher ko project explain karte waqt ye evidence kaam aata hai.

## 6. Deployment Ko End Mein Test Karo

Local machine par pehle ye successfully chalao:
```
train → save → load → predict → UI
```
Phir online deploy karo.

## 7. AI Code Blindly Trust Mat Karo

Har major stage par run karke check karo. Tumne is project mein bhi exactly ye approach follow ki aur isi wajah se errors step-by-step solve hue.

## 8. Credentials/API Keys Kabhi AI Ko Mat Deno

Agar deployment ke liye secret/token chahiye ho to **environment variables/secrets** use karo.

## 9. Final Delivery — 5 Cheezein Zaroor Honi Chahiye

1. GitHub repository
2. Trained model
3. requirements.txt
4. README / project report
5. Live demo link

## 10. Sirf Accuracy Tak Limited Mat Raho

Ek achha ML project = **problem + data + preprocessing + model + evaluation + UI + deployment + documentation**

---

> Tumhara CIFAR-10 project isi complete pipeline ka achha example ban gaya hai.
