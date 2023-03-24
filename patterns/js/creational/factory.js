

class whiteCholocate{
	constructor(brand){
		this.brand = brand
		this.type = "white_cholocate"
	}
}

class darkCholocate{
	constructor(brand){
		this.brand = brand
		this.type = "dark cholocate"
	}
}

class milkCholocate{
	constructor(brand){
		this.brand = brand
		this.type = "milk cholocate"
	}
}



class ChocolateFactory{

	static factory_name = "Wedex"

	static makeWhiteCholocate(brand = ChocolateFactory.factory_name){
		return new whiteCholocate(brand);
	}

	static makeDarkCholocate(brand = ChocolateFactory.factory_name){
		return new darkCholocate(brand);
	}

	static makeMilkCholocate(brand = ChocolateFactory.factory_name){
		return new milkCholocate(brand);
	}

}



const main = ()=>{
	myWhiteBar = ChocolateFactory.makeWhiteCholocate()
	console.log(myWhiteBar)
}
main()