/* JS 배열의 메서드 */

// indexOf, lastIndexOf, includes
const yongdonList = ['할머니', '할아버지', '큰삼촌', '할아버지', '작은숙모', '외삼촌', '할아버지'];
console.log('===== indexOf =====');
console.log(yongdonList.indexOf('할아버지'));
console.log(yongdonList.indexOf('할아버지', 2));
console.log(yongdonList.lastIndexOf('할아버지'));
console.log(yongdonList.includes('할머니'));



// push, pop
console.log('===== push & pop =====');
console.log(yongdonList.push('엄마'), yongdonList);
console.log(yongdonList.push('아빠'), yongdonList);
console.log(yongdonList.pop(), yongdonList);
console.log(yongdonList.pop(), yongdonList);
console.log(yongdonList.pop(), yongdonList);
console.log(yongdonList.pop(), yongdonList);
console.log(yongdonList.pop(), yongdonList);



// unshift, shift
const chikenList = ['후라이드치킨', '양념치킨', '간장치킨'];
console.log('===== shift & unshift =====');
console.log('원래 치킨:', chikenList);
chikenList.unshift('파닭');
chikenList.unshift('마늘치킨');
chikenList.unshift('스노윙치킨', '불닭');
console.log('unshift 후:', chikenList);
console.log(chikenList.shift(), chikenList);
console.log(chikenList.shift(), chikenList);
console.log(chikenList.shift(), chikenList);
console.log(chikenList.shift(), chikenList);
console.log(chikenList.shift(), chikenList);



// concat
// arr1.concat(arr2, ...);



// slice, splice
const frontEnd = ['HTML', 'CSS', 'JavaScript', 'ES6'];
console.log('===== slice & splice =====');
console.log(frontEnd.slice(1, 3));
console.log(frontEnd);
console.log(frontEnd.splice(3, 1, '자바스크립트'));
console.log(frontEnd);



// join
console.log(frontEnd.join('---'));



// reverse
console.log(frontEnd.reverse());
