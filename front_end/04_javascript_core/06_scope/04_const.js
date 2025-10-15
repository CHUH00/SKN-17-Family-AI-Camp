/* const */

/*
    - const 키워드는 상수(constant) 선언을 위해 사용
    - let 키워드와 마찬가지로 블럭 레벨 스코프를 가짐
    - let 키워드와 마찬가지로 변수 호이스팅이 발생하지 않는 것처럼 동작
    (* 상수 == 재할당이 금지된 변수)
*/

// 1. 선언과 동시에 초기화해야 함
const TEST = 1;



// 2. const 키워드로 선언한 변수는 재할당 금지
// TEST = 100;
console.log(TEST);

// const 키워드로 선언한 변수에 '객체'를 할당한 경우
// property 값은 변경 가능 (단, 마찬가지로 재할당은 불가)
const STUDENT = {
    name: "SKN 17기",
    count: 28
};

STUDENT.name = "최종 프로젝트 때 최고의 결과를 보여줄 17기^^";
console.log(STUDENT);

STUDENT['studyTime'] = 960;
console.log(STUDENT);

STUDENT = {};
