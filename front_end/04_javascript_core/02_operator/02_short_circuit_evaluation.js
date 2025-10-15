/* 단축 평가 */
/* 표현식을 평가하는 도중 평가 결과가 확정된 경우 나머지 평가 과정을 생략하는 것 */

/*
    논리연산자
    - AND : &&
    - OR  : ||
    - NOT : !
*/
// OR, AND 연산자 표현식의 결과는 boolean이 아닐 수도 있음



// 'apple'이 이미 Truthy한 값이므로 true로 평가되고
// 논리 연산의 결과를 결정한 피연산자 'apple'을 그대로 반환
console.log(false || 'apple');      // apple
console.log('apple' || false);      // apple
console.log('apple' || 'banana');   // apple

console.log(false && 'apple');      // false
console.log('apple' && false);      // false
console.log('apple' && 'banana');   // banana



// 단축 평가를 사용해 if문 대체 가능
var num = 1;

if (num % 2 == 0) {
    console.log('짝수');
} else {
    console.log('홀수');
}

num % 2 == 0 && console.log('짝수');
num % 2 == 0 || console.log('홀수');



// 객체를 가리키기를 기대하는 변수가 null 또는 undefined가 아닌지 확인하고
// 프로퍼티를 참조할 때 단축 평가를 유용하게 활용 가능
var obj = null;
// console.log(obj.value);
obj && console.log(obj.value);
