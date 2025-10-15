/* optional chaining operator */

/*
    ?.
    - ES11(EcmaScript2020)에서 도입된 연산자
    - 좌항의 피연산자가 null 또는 undefined인 경우 undefined 반환
    - 그렇지 않으면 우항의 프로퍼티 참조 이어감
*/

var obj = null;

// var val = obj.value;             // TypeError
// var val = obj && obj.value;      // 단축 평가로 해결
var val = obj?.value;

// console.log(val);



// 논리연산자 &&를 이용한 단축 평가에서는 
// 빈 문자열 같은 Falsy한 값을 false 취급해서 문제 발생
// => 옵셔널 체이닝이 해결
var str = '';

var len = str && str.length;    // 단축 평가 이용: len == ''
len = str?.length;              // 옵셔널 체이닝 이용: len == 0

console.log(len);
