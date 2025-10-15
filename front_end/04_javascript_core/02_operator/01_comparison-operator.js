/* 비교 연산자 */

/*
    - 동등 비교(==, !=): 값이 같은지 비교 (암묵적 형변환 비교)
    - 일치 비교(===, !==): 타입과 값이 모두 같은지 비교
*/

console.log("===== 숫자 1과 문자 '1', true 비교 =====");
console.log(`1 == '1' : ${1 == '1'}`);     // T
console.log(`1 == true : ${1 == true}`);   // T
console.log(`1 === '1' : ${1 === '1'}`);   // F
console.log(`1 === true : ${1 === true}`); // F

console.log("===== 숫자 0과 빈 문자열 '', 문자 '0', false 비교 =====");
console.log(`0 == '0' : ${0 == '0'}`);       // T
console.log(`0 == '' : ${0 == ''}`);         // T
console.log(`0 == false : ${0 == false}`);   // T
console.log(`0 === '0' : ${0 === '0'}`);     // F
console.log(`0 === '' : ${0 === ''}`);       // F
console.log(`0 === false : ${0 === false}`); // F

console.log("===== NaN과 NaN 비교 =====")
// NaN은 자신과 일치하지 않는 유일한 값
console.log(`NaN == NaN : ${NaN == NaN}`);               // F
console.log(`NaN === NaN : ${NaN === NaN}`);             // F
console.log(`Number.isNaN(NaN) : ${Number.isNaN(NaN)}`); // T
