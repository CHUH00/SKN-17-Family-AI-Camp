/* 스프레드 문법 (전개 문법 / spread syntax) */

console.log(Math.max(10, 30, 20, 123981));

var arr = [10, 20, 30, 2931, 202, 391];
console.log(Math.max(arr));
console.log(Math.max(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]));
console.log(Math.max(...arr));

var arr1 = [1, 2, 3, 4, 5];
var arr2 = [-1, -2, -3, -4, -5];
console.log(Math.min(...arr1, ...arr2));

console.log(Math.min(...arr1, -2025, 10, 2, ...arr2, 9, 33));



// 배열 병합에 사용 가능
var mergedArr = [...arr1, ...arr2];
// mergedArr = arr1 + arr2;
// mergedArr = arr1.concat(arr2);
console.log(mergedArr);



// Array.from()처럼 이터러블 배열 변환에 사용 가능
var str = "JavaScript";
console.log(Array.from(str));
console.log([...str]);
