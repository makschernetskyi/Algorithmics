

class Unique {
	constructor(data){
		if(Unique.exists){
			return Unique.instance
		}
		Unique.instance = this
		Unique.exists = true
		this.data = data
	}

	getData(){
		return this.data
	}
}

class dog{
	constructor(){}
}



(function(){

	// initializing the only possible instance of class unique
	const instance = new Unique(
		{users:[{username: "george"}, {username: "mary"}]}
	)

	console.log(JSON.stringify(instance.getData()))



	const secondInstance = new Unique(
		{users:[{username: "vallery"}]}
	)

	console.log(JSON.stringify(secondInstance.getData()))
	// secondInstance is still just the first instance


})();



