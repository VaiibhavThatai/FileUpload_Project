document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("upload-form");
    const fileInput = document.getElementById("file-input");
    const fileInfo = document.getElementById("file-info");
    const uploadedFiles = document.getElementById("uploaded-files");

    uploadForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const formData = new FormData(uploadForm);
        
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();

        fileInfo.textContent = result.message;

        if (result.message === "Files successfully uploaded") {
            updateUploadedFiles();
        }
    });

    async function updateUploadedFiles() {
        const response = await fetch("/files");
        const files = await response.json();
        
        uploadedFiles.innerHTML = "";
        
        files.forEach(file => {
            const fileDiv = document.createElement("div");
            fileDiv.innerHTML = `
                <p><strong>Filename:</strong> ${file.filename}</p>
                <p><strong>Size:</strong> ${formatSize(file.size)}</p>
                <p><strong>URL:</strong> <a href="${file.url}" target="_blank">Open</a></p>
            `;
            uploadedFiles.appendChild(fileDiv);
        });
    }

    function formatSize(bytes) {
        const sizes = ["Bytes", "KB", "MB", "GB", "TB"];
        if (bytes === 0) return "0 Byte";
        const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
        return Math.round(bytes / Math.pow(1024, i), 2) + " " + sizes[i];
    }

    updateUploadedFiles();
});
