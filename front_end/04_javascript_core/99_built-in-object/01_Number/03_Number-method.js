/* 01. Number - method */

// Number.isFinite : 인수로 전달된 숫자값이 정상적인 유한수인지 검사하여 결과를 불리언으로 반환
console.log(Number.isFinite(10));
console.log(Number.isFinite(-10));
console.log(Number.isFinite(Infinity));
console.log(Number.isFinite(-Infinity));
console.log(Number.isFinite(NaN));

console.log(Number.isFinite(null));

console.log(isFinite(null));            // 빌트인 전역함수 isFinite는 암묵적 타입변환을 한다

console.log('----------------------');



// Number.isInteger : 인수로 전달된 숫자값이 정수인지 검사하여 결과를 불리언으로 반환
console.log(Number.isInteger(10));
console.log(Number.isInteger(-10));
console.log(Number.isInteger(10.10));
console.log(Number.isInteger(-10.10));
console.log(Number.isInteger('10'));
console.log(Number.isInteger(false));
console.log(Number.isInteger(Infinity));
console.log(Number.isInteger(-Infinity));

console.log('----------------------');



// Number.isNaN : 인수로 전달된 숫자값이 NaN인지 검사하여 결과를 불리언으로 반환
console.log(Number.isNaN(NaN));
console.log(Number.isNaN(undefined));
console.log(isNaN(undefined));              // 빌트인 전역함수 isNaN은 암묵적 타입변환을 한다

console.log('----------------------');



// Number.isSafeInteger : 인수로 전달된 숫자값이 안전한 정수인지 검사하여 결과를 불리언으로 반환
console.log(Number.isSafeInteger(10));
console.log(Number.isSafeInteger(1000000000000000000000));
console.log(Number.isSafeInteger(10.10));
console.log(Number.isSafeInteger('10'));
console.log(Number.isSafeInteger(false));
console.log(Number.isSafeInteger(Infinity));

console.log('----------------------');



// Number.prototype.toExponential : 숫자를 지수 표기법으로 변환하여 문자열로 반환
// e 앞에 있는 숫자에 10의 n승을 곱하는 형식으로 수를 나타낸다
console.log((1.23456).toExponential());

// 소수점 이하로 표현할 자리수 전달한다.
console.log((1.23456).toExponential(3));
console.log((1.23456).toExponential(1));

console.log('----------------------');



// Number.prototype.toFixed : 숫자를 반올림하여 문자열로 반환한다
// 반올림 하는 소수점 이하 자리수를 나타내는 0~20 사이의 정수값을 인수로 전달할 수 있다
console.log((1.23456).toFixed());
console.log((1.23456).toFixed(3));
console.log((1.23456).toFixed(1));

console.log('----------------------');



// Number.prototype.toPrecision : 인수로 전달받은 전체 자릿수까지 유효하도록 나머지 자릿수를 반올림하여 문자열로 반환
// 0~21 사이의 정수 값을 인수로 전달할 수 있으며 생략하면 기본값 0이 지정된다
console.log((123.456).toPrecision());
console.log((123.456).toPrecision(5));
console.log((123.456).toPrecision(3));
console.log((123.456).toPrecision(1));

console.log('----------------------');



// Number.prototype.toString : 숫자를 문자열로 변환하여 반환한다
// 진법을 나타내는 2~36 사이의 정수값을 인수로 전달할 수 있다
console.log((100).toString());
console.log((100).toString(2));
console.log((100).toString(8));
console.log((100).toString(16));

console.log('----------------------');
