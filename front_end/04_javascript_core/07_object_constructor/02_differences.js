/* 생성자 함수 vs 일반 함수 */

function Student(name, hobby) {
    this.name = name;
    this.hobby = hobby;
    this.getInfo = function() {
        return `${this.name}의 취미는 ${this.hobby}입니다.`;
    };
}

// new 연산자와 함께 호출해야 함
// - new 연산자와 함께 호출해야 생성자 함수로써 동작
// - 그렇지 않으면 일반 함수로 동작
const student = Student('다람쥐', '야구보기');
console.log(student);
console.log(hobby);

const newStudent = new Student('람쥐썬더', '공부하기');
console.log(newStudent);
console.log(hobby);



// new.target (ES6)
// - new 연산자와 함께 생성자 함수로써 호출 시, 함수 자기 자신
// - new 연산자 없이 일반 함수로써 호출 시, undefined
function Dog(name, skill) {

    console.log(new.target);
    if(!new.target) {
        return new Dog(name, skill);
    }

    this.name = name;
    this.skill = skill;
}

const dog = Dog('뽀삐', '손!');
console.log(dog);

const newDog = new Dog('삐뽀', '빵!');
console.log(newDog);



// 내장 생성자 함수는 new 연산자 없이 사용해도 빈 객체를 반환하는 방식으로 잘 동작하게 만들어짐
const obj = Object();
console.log(obj);
