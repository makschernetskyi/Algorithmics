


function Animal(name, species){

	if(!(this instanceof Animal)){
		return new Animal(name, species)
	}

	this.name = name
	this.species = species

	//alternative implementation of a method
	/* this.getName = function(){
		return this.name;
	}
	*/

}

Animal.prototype.getName = function(){
		return this.name;
}


function main(){

	const myDog = new Animal('camilla', 'retriever')

	console.log(myDog.getName())
	console.log(myDog)


}
main();








