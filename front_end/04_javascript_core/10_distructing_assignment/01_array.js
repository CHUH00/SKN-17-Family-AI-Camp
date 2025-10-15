/* Array Distructuring Assignment (배열 구조 분해 할당) */

// [ 기본 문법 ]
let nameArr = ['Squirrel', 'Nam'];

// let firstName = nameArr[0];
// let lastName = nameArr[1];

let [firstName, lastName] = nameArr;

console.log(`저는 ${lastName}가 ${firstName} 입니다.`);

// 일부 추출
let lunchSet = ['더블비프치즈버거', '감자튀김', '콘샐러드', '제로콜라'];
let [burger, , , drink] = lunchSet;
console.log(`나는 다이어트 중이라 ${burger}랑 ${drink}만 먹을게 ^_^!`);



// 활용 1: 객체 프로퍼티 할당
let user = {};
[user.lastName, user.firstName] = "Nam Yunjin".split(" ");
console.log(user);

// 활용 2: Object.entries()와 조합
console.log(Object.entries(user));

for (let [key, value] of Object.entries(user)) {
    console.log(value);
}

// 활용 3: 변수 교환
let cup1 = '아샷추';
let cup2 = '카페라떼';

// 불가
// cup1, cup2 = cup2, cup1;

// 구조 분해 할당을 하지 않을 때의 기존 방식
// let temp = cup1;
// cup1 = cup2;
// cup2 = temp;

[cup1, cup2] = [cup2, cup1];
console.log(cup1, cup2);

// 활용 4: rest parameters와 조합
let [king, queen, jack, ace, ...numbers] = ['KING', 'QUEEN', 'JACK', 'ACE', 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(king);
console.log(queen);
console.log(jack);
console.log(ace);
console.log(numbers);

// 활용 5: 기본값 설정 가능
let userArr = ['다람쥐', 190, '서울시 금천구'];
let [name, height, address, job='강사', skill='LLM'] = userArr;
console.log(name, height, address, job, skill);
