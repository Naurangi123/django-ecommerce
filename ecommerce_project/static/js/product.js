function updateTotalPrice(input, productPrice) {
    const quantity = input.value;
    const totalPriceElement = input.closest('.cart-info').querySelector('.total-price');
    const totalPrice = productPrice * quantity;
    totalPriceElement.textContent = totalPrice.toFixed(2); // Format to 2 decimal places
}
updateTotalPrice(this,item.product.price)