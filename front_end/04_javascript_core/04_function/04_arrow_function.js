/* 화살표 함수 (arrow function) */

var message;

message = function() {
    return "Hello World!";
};
console.log('function', message());

// 화살표 함수 기본 형식
message = () => {
    return "Hello World!";
};
console.log('arrow function', message());

// 함수 수행 내용이 return 뿐이라면
// return 키워드 생략 가능 + 함수블럭(중괄호) 생략 가능
// 단, 파라미터가 없더라도 화살표 앞 ()는 생략 불가
message = () => "Hello World!";
console.log('arrow function without {}', message());

message = (str1, str2) => str1 + "Hello World!" + str2;
console.log('arrow function with params', message("파라미터 ", " 전달 완료!"));

// 하지만 파라미터가 단 1개인 경우에는 화살표 앞 ()도 생략 가능
message = str1 => str1 + "Hello World!";
console.log('arrow function with param', message("파라미터 "));

// 반환값이 object인 경우에는 
// return 키워드와 코드블럭{}을 생략하려면 ()로 감싸줘야 함
var createUser = (name, hobby) => ({name, hobby});
console.log(createUser('다람쥐', 100));

// 화살표 함수는 코드 수행 내용이 한 줄인 함수에 유용하며
// 고차 함수의 인자(콜백 함수)로 많이 활용됨
console.log(
    [1, 2, 3, 4, 5].map(function(val) { return val * 10 })
);

console.log(
    [1, 2, 3, 4, 5].map(val => val * 10)
);
