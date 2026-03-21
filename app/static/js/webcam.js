const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const snap = document.getElementById("snap");
const result = document.getElementById("result");

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(error => {
    result.innerText = "無法開啟攝影機: " + error;
  });

snap.onclick = function () {
  const context = canvas.getContext("2d");
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
        if (data.status === "success") {
          result.innerText = `打卡成功：${data.name}，時間：${data.time}`;
        } else {
          result.innerText = "辨識失敗，查無此人";
        }
      })
      .catch(error => {
        result.innerText = "打卡失敗: " + error;
      });
  }, "image/jpeg");
};