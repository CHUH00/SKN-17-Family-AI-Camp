/* 연산자 (in) */

var actor = {
    name: '차은우',
    age: 30,
    gender: 'M',
    company: undefined
};

console.log(actor.name === undefined);
console.log(actor.drama === undefined);
console.log(actor.company === undefined);

// 프로퍼티 존재 여부 확인 가능
console.log('name' in actor);
console.log('drama' in actor);
console.log('company' in actor);



// for-in 반복문
// 객체의 key를 순회하며 받음
for (var key in actor) {
    console.log(key);
    console.log(actor[key]);
}
