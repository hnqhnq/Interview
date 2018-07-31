// 8.采用递归的方式用javascript写一下快速排序算法
// 基准
// 遍历分出两个数组
// 递归
// var arr=[10,2,44,2]
function quickSort(arr) {
    //取基准
    var pointIndex = Math.floor(arr.length / 2);
    //数组去除基准元素，并取出其值
    var pointValue = arr.splice(pointIndex, 1)[0];
    var left = [],
        right = [];
    for (var i = 0, length = arr.length; i < length; i++) {
        arr[i] < pointValue ? left.push(arr[i]) : right.push(arr[i]);
    }
    return quickSort(left).concat([pointValue], quickSort(right));
}

/* ***********************************************       */

// quickSort(arr)
function QuickSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }
    var self = arguments.callee;
    var left = [], right = [], middle = [];
    var mid = arr[Math.floor(arr.length / 2)];

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < mid) {
            left.push(arr[i])
        } else if (arr[i] > mid) {
            right.push(arr[i]);
        } else {
            middle.push(arr[i]);
        }
    }
    return [].concat(self(left), middle, self(right));

}

var arrtest = [1, 7, 2, 9, 4, 8];
QuickSort(arrtest);
