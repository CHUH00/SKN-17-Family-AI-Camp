/* 배열 */

// 1. 배열 리터럴
const arr = ['다람쥐', '토끼', '호랑이'];
console.log(arr);



// 2. 배열 생성자 함수
const arr2 = new Array();
console.log(arr2);

const arr2_1 = new Array(10);           // 10칸짜리 빈 배열 (length 프로퍼티 지정)
const arr2_2 = new Array(10, 20, 30);   // 인자를 요소로 가지는 배열
const arr2_3 = new Array('javascript'); // 인자를 요소로 가지는 배열
console.log(arr2_1);
console.log(arr2_2);
console.log(arr2_3);



// 3. Array.of() 메서드
const arr3_1 = Array.of(10);
const arr3_2 = Array.of(10, 20, 30);
const arr3_3 = Array.of('javascript');
console.log(arr3_1);
console.log(arr3_2);
console.log(arr3_3);



// 배열 == object
console.log(typeof arr);

/*
    [ 프로퍼티 플래그 ]
    객체 프로퍼티는 값(value)과 함께 플래그(flag)라는 특별한 속성 세 가지를 가짐
    - writable: 수정 가능 여부 (true: 값 수정 가능 / false: 읽기만 가능)
    - enumerable: 반복문을 사용해 나열 가능한지 여부
    - configurable: 프로퍼티 삭제 및 플래그 수정 가능 여부
*/
console.log(Object.getOwnPropertyDescriptors(arr));
