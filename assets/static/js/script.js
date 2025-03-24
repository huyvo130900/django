// script.js

// Hàm để hiển thị thông báo khi nhấp vào nút
document.addEventListener("DOMContentLoaded", function() {
    const btn = document.querySelector('.btn');
    
    if (btn) {
        btn.addEventListener('click', function(event) {
            event.preventDefault(); // Ngăn chặn hành động mặc định của nút
            alert("Bạn đã nhấp vào nút Khám Phá Dịch Vụ!");
            // Bạn có thể thêm mã để chuyển hướng đến trang dịch vụ ở đây
            // window.location.href = "services.html";
        });
    }
});