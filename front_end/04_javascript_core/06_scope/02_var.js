/* var */

// 1. 변수 중복 선언 허용
var msg = "열심히 공부해 봅시다!";
console.log(msg);

var msg = "곧 최종 프로젝트니까요!";
console.log(msg);

// 초기화문이 없는 변수 선언문은 중복 선언하면 무시됨
var msg;
console.log(msg);



// 2. 함수 레벨 스코프 (함수 코드 블록만 지역 스코프 인정)



//  3. 변수 호이스팅
console.log(test);
test = "테스트 출력";
console.log(test);
var test;
