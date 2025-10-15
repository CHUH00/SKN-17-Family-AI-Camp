/* 매개변수(Parameter)와 인자(Arguments) */

function lunch(menu) {
// function lunch(...menu) {   // 가변인자
    console.log('lunch가 몰래 갖고 있는 args:', arguments);
    // arguments: 함수 내부적으로 가지고 있는 인자값을 다 저장한 객체
    console.log('lunch가 받은 menu:', menu);
    return `오늘 점심은 ${menu}를 먹었어. 아주 맛있더라고~`;
}

console.log(lunch('김밥'));
console.log(lunch());                                   // 인자가 부족해서 할당되지 않으면 undefined
// console.log(menu);                                   // 파라미터 값은 함수 내부에서만 사용 가능
console.log(lunch('양꼬치', '양갈비', '소갈비', '채끝살')); // 파라미터보다 많은 인자는 무시됨



function dance(danceName = '꼭짓점댄스') {

    // 인자 검증
    // 1. 인자를 1개만 받아야 해
    // 2. 1개의 인자는 문자열이어야 해
    // 3. 빈 문자열이면 안돼
    if(arguments.length !== 1 || 
       typeof danceName !== 'string' || 
       danceName.length === 0
    ) {
        throw new TypeError('잘못된 인자 전달 딱 걸렸음!!!');
    }

    return `${danceName} 춤추기 시작💃🕺🪩`;
}

result = dance('');
console.log(result);