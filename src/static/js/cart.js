// var updateBtn = document.getElementsByClassName('update-cart')
// for (var i = 0 ; i < updateBtn.length; i++){
//     updateBtn[i].addEventListener('click', function(){
//         var productId = this.dataset.product
//         var action = this.dataset.action
//         console.log('prdcutId', productId, 'action', action)

//         console.log('User', user)
//         if (user == 'AnonymousUser'){
//             console.log('not loged in')
//         }else{
//             updateUserOrder(productId, action)
//         }
//     })
// }

// function updateUserOrder(productId, action){
//     console.log('user is logged in, sending data...')
//     var url = '/update_item/'

//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type' : 'application/Json',
//             'X-CSRFToken' : csrftoken,
//         },
//         body:JSON.stringify( {
//             'productId': productId, 'action' : action 
//         })
//     })
//     .then((response) => {
//         return response.json()
//     })

//     .then((data) => {
//         console.log('data:', data)    
//     })
// }


var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
        .then(console.log('here'))
		.then((response) => {
		   return response.json();
		})
        .then(console.log('here1'))
		.then((data) => {
		    console.log('data:', data) 
		});
}