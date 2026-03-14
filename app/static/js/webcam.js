const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');
const result = document.getElementById('result');

navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    video.srcObject = stream;
});

snap.onclick = function() {

    const context = canvas.getContext('2d');

    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(blob => {

        const formData = new FormData();

        formData.append("image", blob, "capture.jpg");

        fetch("/checkin", {
            method: "POST",
            body: formData
        })
        .then(res => res.json())
        .then(data => {

            if(data.name === "Unknown"){
                result.innerText = "辨識失敗"
            }else{
                result.innerText = "打卡成功: " + data.name + " " + data.time
            }

        });

    });

};