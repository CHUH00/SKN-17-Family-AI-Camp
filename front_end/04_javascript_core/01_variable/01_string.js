// JS 한 줄 주석 

/*
    JS 여러 줄 주석
*/



/* 문자열 타입 */

var string;
string = 'JavaScript "큰 따옴표" 자체로 출력';
string = "JavaScript '작은 따옴표' 자체로 출력";
string = `JavaScript`;

console.log(string);

/* 템플릿 리터럴 */
/*
    ES6부터 도입된 백틱(``)을 사용한 표현식으로
    멀티라인 문자열, 표현식 삽입 등
    편리한 문자열 처리 기능을 제공하는 문자열 표기법
*/

// var str = '안녕하세요.
// 다람쥐입니다.';
var str = '안녕하세요. \n다람쥐입니다.';
console.log(str);

var multiline = `안녕하세요.
진짜 다람쥐입니다.`;
console.log(multiline);

var teacher = '다람쥐';
var student = 17;

// 다람쥐 선생님과 함께 하는 17기의 SKN 일대기!
console.log(teacher + " 선생님과 함께 하는 " + student + "기의 SKN 일대기!");
console.log(`${teacher} 선생님과 함께 하는 ${student}기의 SKN 일대기!`);
// console.log('${teacher} 선생님과 함께 하는 ${student}기의 SKN 일대기!');
