/* 스프레드 문법을 이용한 배열/객체 복사 */

// 배열 복사
var arr = [2025, 10, 2];
var arrCopy1 = arr;         // 얕은 복사
var arrCopy2 = [...arr];    // 깊은 복사

arrCopy1.push(944);
console.log(arr, arrCopy1);

arrCopy2.push(945);
console.log(arr, arrCopy2);



// 객체 복사
var obj = {
    name: '다람쥐',
    job: '선생님'
};

var objCopy1 = obj;         // 얕은 복사
var objCopy2 = {...obj};    // 깊은 복사

objCopy1['job'] = '댄스가수';
console.log(obj, objCopy1);

objCopy2['job'] = '뮤지컬배우';
console.log(obj, objCopy2);
