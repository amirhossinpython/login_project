function validateForm() {
    // گرفتن مقادیر فرم
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    const nationalCode = document.getElementById('national_code').value;
    const phone = document.getElementById('phone').value;
    const age = document.getElementById('age').value;
    
    // اعتبارسنجی رمز عبور
    if (password !== confirmPassword) {
        alert('رمز عبور و تکرار آن مطابقت ندارند!');
        return false;
    }
    
    if (password.length < 6) {
        alert('رمز عبور باید حداقل ۶ کاراکتر باشد');
        return false;
    }
    
    // اعتبارسنجی کد ملی
    if (!/^\d{10}$/.test(nationalCode)) {
        alert('کد ملی باید ۱۰ رقم باشد');
        return false;
    }
    
    // اعتبارسنجی شماره موبایل
    if (!/^\d{11}$/.test(phone)) {
        alert('شماره موبایل باید ۱۱ رقم باشد');
        return false;
    }
    
    // اعتبارسنجی سن
    if (age < 1 || age > 120) {
        alert('لطفاً سن معتبر وارد کنید');
        return false;
    }
    
    return true;
}

// اعتبارسنجی لحظه‌ای برای کد ملی
document.addEventListener('DOMContentLoaded', function() {
    const nationalCodeInput = document.getElementById('national_code');
    if (nationalCodeInput) {
        nationalCodeInput.addEventListener('input', function(e) {
            this.value = this.value.replace(/[^0-9]/g, '');
        });
    }
    
    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            this.value = this.value.replace(/[^0-9]/g, '');
        });
    }
});