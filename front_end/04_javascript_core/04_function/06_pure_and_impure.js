/* 순수 함수 & 비순수 함수 */

/*
    - 순수 함수: 외부 상태에 의존하지도 않고 외부 상태를 변경하지도 않는 함수
    - 비순수 함수: 외부 상태에 의존하거나 외부 상태를 변경하는 함수
*/

var cnt = 0;

// 순수 함수
function increase(n) {
    return ++n;
}

increase(cnt);
console.log(cnt);

cnt = increase(cnt);
console.log(cnt);

// 비순수 함수
function decrease() {
    return --cnt;
}

decrease();
console.log(cnt);

cnt = decrease();   // 재할당이 불필요 (함수 호출만 해도 같은 결과)
console.log(cnt);
