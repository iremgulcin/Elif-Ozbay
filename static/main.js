const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

async function setupCamera() {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        throw new Error('Browser API navigator.mediaDevices.getUserMedia not available');
    }

    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
}

async function detectEmotions() {
    const model = await tf.loadLayersModel('{{ url_for("static", filename="model.json") }}');
    const faceDetector = await tf.loadGraphModel('{{ url_for("static", filename="haarcascade_frontalface_default.json") }}');
    const emotionLabel = document.getElementById('emotion-label');

    while (true) {
        context.drawImage(video, 0, 0, 640, 480);
        const imgData = context.getImageData(0, 0, 640, 480);

        const faces = await faceDetector.detectSingleFace(imgData);

        if (faces) {
            const emotions = model.predict(preprocess(faces)).dataSync();
            const dominantEmotion = getDominantEmotion(emotions);
            emotionLabel.innerText = `Detected emotion: ${dominantEmotion}`;
        }

        await tf.nextFrame();
    }
}

function preprocess(faces) {
    return faces;
}

function getDominantEmotion(emotions) {
    const emotionLabels = ['Kizgin', 'Igrenme', 'Korku', 'Mutlu', 'Normal', 'Uzgun', 'Sasirmis'];
    const maxIndex = emotions.indexOf(Math.max(...emotions));
    return emotionLabels[maxIndex];
}



setupCamera();
detectEmotions();
