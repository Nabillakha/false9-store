function showToast(title, message, type = "info", duration = 3500) {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = `
    flex items-start gap-3 px-5 py-3 rounded-xl shadow-lg text-sm
    animate-slide-up opacity-0 transform transition-all duration-500
    ${getToastStyle(type)}
  `;

  toast.innerHTML = `
    <div class="text-xl">${getToastIcon(type)}</div>
    <div>
      <p class="font-semibold">${title}</p>
      <p class="text-gray-700 text-sm">${message}</p>
    </div>
  `;

  container.appendChild(toast);

  // animasi masuk
  setTimeout(() => {
    toast.classList.remove("opacity-0", "translate-y-4");
    toast.classList.add("opacity-100", "translate-y-0");
  }, 10);

  // animasi keluar
  setTimeout(() => {
    toast.classList.remove("opacity-100", "translate-y-0");
    toast.classList.add("opacity-0", "translate-y-4");
    setTimeout(() => toast.remove(), 500);
  }, duration);
}

// Style warna per jenis toast
function getToastStyle(type) {
  switch (type) {
    case "success":
      return "bg-green-50 border-l-4 border-green-500 text-green-800";
    case "error":
      return "bg-red-50 border-l-4 border-red-500 text-red-800";
    case "warning":
      return "bg-yellow-50 border-l-4 border-yellow-500 text-yellow-800";
    case "info":
      return "bg-blue-50 border-l-4 border-blue-500 text-blue-800";
    default:
      return "bg-gray-50 border-l-4 border-gray-400 text-gray-700";
  }
}

// Icon berbeda tiap tipe
function getToastIcon(type) {
  switch (type) {
    case "success":
      return "✅";
    case "error":
      return "❌";
    case "warning":
      return "⚠️";
    case "info":
      return "ℹ️";
    default:
      return "🔔";
  }
}

/* ================================
   🎯 Versi Khusus untuk Event App
   ================================ */

// Add Product
function showAddProductToast(success = true) {
  if (success) {
    showToast("Product Added!", "Your product has been successfully added.", "success");
  } else {
    showToast("Error", "Failed to add product.", "error");
  }
}

// Edit Product
function showEditProductToast(success = true) {
  if (success) {
    showToast("Product Updated!", "Your product details have been updated.", "success");
  } else {
    showToast("Error", "Failed to update product.", "error");
  }
}

// Delete Product
function showDeleteProductToast(success = true) {
  if (success) {
    showToast("Deleted", "The product has been deleted.", "warning");
  } else {
    showToast("Error", "Failed to delete product.", "error");
  }
}

// Login
function showLoginToast(success = true) {
  if (success) {
    showToast("Welcome Back!", "You’ve successfully logged in.", "success");
  } else {
    showToast("Login Failed", "Invalid username or password.", "error");
  }
}

// Logout
function showLogoutToast() {
  showToast("Logged Out", "You’ve been successfully logged out.", "info");
}

// Register
function showRegisterToast(success = true) {
  if (success) {
    showToast("Account Created!", "Your account has been successfully registered.", "success");
  } else {
    showToast("Error", "Failed to register. Please try again.", "error");
  }
}
