let updateButtons = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateButtons.length; i++) {
  updateButtons[i].addEventListener('click', function () {
    let productId = this.dataset.product
    let action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
  })
}
