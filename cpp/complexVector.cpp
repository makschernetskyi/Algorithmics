class ComplexVector {

	complex<float> *arr;
	int capacity;
	int current;

public:
	ComplexVector() {
		arr = new complex<float>[1];
		capacity = 1;
		current = 0;
	}

	~ComplexVector() {
		delete[] arr;
	}

	void push(complex<float> element) {

		if (current == capacity) {
			complex<float> *temp = new complex<float>[2 * capacity];


			for (int i = 0; i < capacity; i++) {
				temp[i] = arr[i];
			}

			delete[] arr;
			capacity *= 2;
			arr = temp;
		};

		arr[current] =
				element;
		current++;
	}

	complex<float> pop() {
		current--;
		return arr[current + 1];
	}

	int size() {
		return current;
	}

	complex<float> getEntry(int index) {
		return arr[index];
	}

	void setEntry(int index, complex<float> element) {
		arr[index] = element;
	}

	static complex<float> scalarProduct(ComplexVector &a, ComplexVector &b) {
		complex<float> result(0, 0);
		for (int i = 0; i < a.size(); i++) {
			result += a.getEntry(i) * b.getEntry(i);
		}
		return result;
	}

	static ComplexVector sum(ComplexVector &a, ComplexVector &b) {
		ComplexVector result;
		for (int i = 0; i < a.size(); i++) {
			result.push(a.getEntry(i) + b.getEntry(i));
		}
		return result;
	}

	void print() {
		for (int i = 0; i < current; i++) {
			cout << arr[i].real() << "+" << arr[i].imag() << "i" << " ";
		}
	}
};