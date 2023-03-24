

class Factory{

	constructor(capacity){
		this.products = [];
		this._prepare_n_products(capacity);
	}



	_prepare_n_products(n){
		for(let i = 0; i<n; i++){
			this.products.push(this.createProduct());
		};
	}

	advertise_products(){
			console.log(`Only today limited offer for ${this.products[0]?.name}, hurry up, only ${this.products.length} left!!!`);
	}

	createProduct(){
		throw new Error(
			'not Implemented',
			"the method you are calling wasn't Implemented yet"
		);
	}
}


class Shirt{
	constructor(){
		this.name = 'shirt'
	}
}

class Hoodie{
	constructor(){
		this.name = 'Hoodie'
	}
}



class ShirtsFactory extends Factory{
	constructor(capacity){
		super(capacity);
	}

	createProduct(){
		const product = new Shirt();
		return product;
	}

}



class HoodieFactory extends Factory{
	constructor(capacity){
		super(capacity);
	}

	createProduct(){
		const product = new Hoodie();
		return product;
	}

}




const main = () => {

	const shirtsFactory = new ShirtsFactory(10);
	const hoodieFactory = new HoodieFactory(7);

	shirtsFactory.advertise_products();
	hoodieFactory.advertise_products();


}

main()