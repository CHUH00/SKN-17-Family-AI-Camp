/* property */

// 객체 == 프로퍼티의 집합
// 프로퍼티 == 키(key): 값(value)

var idol = {
    group: 'BTS',
    '@ s o n g @': 'Fire',  // 특수문자도 key로 사용 가능 (단, ''로 감싸야 함)
    '': '',                 // 빈 문자열도 key로 사용 가능
    0: 1,                   // 숫자 key는 내부적으로 문자열로 변환됨
    var: 'var',             // 예약어도 key로 사용 가능
    group: '방탄소년단'      // 이미 존재하는 key를 중복 선언하면 나중에 선언한 프로퍼티로 덮어씀
};

// 프로퍼티 동적 추가
var key = 'count';
idol[key] = 7;

console.log(typeof idol);
console.log(idol);



/* 프로퍼티 접근 방식 */

// 마침표 표기법
console.log(idol.group);

// 대괄호 표기법 (프로퍼티 키는 반드시 따옴표로 감싼 문자열 사용)
// console.log(idol.0);
// console.log(idol.'0');
console.log(idol['0']);



/* 프로퍼티 값 단축 구문 (ES6) */
var productName = 'iPhone17';
var price = 1000000;

var product = {
    productName: productName,
    price: price
};

console.log(product);

// 프로퍼티 값으로 변수를 사용하는 경우
// 변수 이름과 프로퍼티 key가 동일한 이름일 때 프로퍼티 key 생략 가능
var new_product = {
    productName, price
};

console.log(new_product);



/* 계산된 프로퍼티 key (ES5) */
// 계산된 프로퍼티 key로 프로퍼티를 동적 생성 가능 (대괄호 표기법 사용)
var prefix = 'B';
var index = 1;

var boardObj = {};

boardObj[prefix + '-' + index++] = '게시글 1';
boardObj[prefix + '-' + index++] = '게시글 2';
boardObj[prefix + '-' + index++] = '게시글 3';

console.log(boardObj);

// ES6
// 객체 리터럴 내부에서도 계산된 프로퍼티 key로 key 동적 생성 가능
var new_boardObj = {
    [`${prefix}-${index++}`] : '게시글 4',
    [`${prefix}-${index++}`] : '게시글 5',
    [`${prefix}-${index++}`] : '게시글 6',
};

console.log(new_boardObj);
