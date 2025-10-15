/* 함수 선언 (function declaration) */

function hello(name) {
    return `${name}님 안녕하세요 :)`;
}

// JS엔진은 생성된 함수를 호출하기 위해 
// 함수 이름과 동일한 식별자를 암묵적으로 생성하고 거기에 함수 객체를 할당함
/*
    var hello = function hello(name) {
        return `${name}님 안녕하세요 :)`;
    };
*/



/* 함수 표현식 (function expression) */
/*
    - var 변수 = 함수; (단, 함수명 생략 가능)
    - 변수명에 해당하는 식별자로 함수 호출해야 함
    - 함수명을 생략하지 않아도 문제는 없지만 함수 호출은 식별자(변수)로만 가능함
*/

var hi = function new_hello(name) {     // 함수명 명시 가능 (호출/참조 시 사용 불가)
    return `${name}야 안녕!!!`;
}; 

hi = function (name) {                  // 함수명 생략 가능 (식별자로 참조/호출)
    return `${name}야 안녕!!!`;
}; 

console.log(hello('다람쥐'));
console.log(hi('다람쥐'));
// console.log(new_hello('다람쥐'));    // ReferenceError
