/* nullish coalescing operator */

/*
    ??
    - ES11(ECMAScript2020)에서 도입된 연산자
    - 좌항의 피연산자가 null 또는 undefined인 경우 우항의 피연산자 반환
    - 그렇지 않으면 좌항의 피연산자 반환
    - 변수 기본값 설정 시 유용
*/

var test = null ?? 'default';
console.log(test);



// 단축 평가 ||를 사용해 기본값을 설정하는 방식은
// 아래와 같은 빈 문자열을 false로 취급해 기본 값이 할당되는 문제 발생
// => nullish coalescing 방식이 해결
var str = '';

var value = str || 'default';
value = str ?? 'default';

console.log(value);
