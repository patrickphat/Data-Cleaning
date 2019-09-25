## Thông tin nhóm

Nhóm 8

Nguyễn Trường Phát `17520880`

Nguyễn Chí Bảo `17520271`

## Dữ liệu

- Nằm ở 3 thư mục `dataset-1`, `dataset-2` và `dataset-3` 
- Mỗi thư mục chứa 1 file dữ liệu đuôi `.data` và 1 file mô tả tên là `info.txt`

## Bài tập 1 - Hiểu dữ liệu

### Tập dữ liệu 1

- Tập dữ liệu được thu thập về thông tin của các loại xe về các thuộc tính của chúng, từ thông tin này chúng ta có thể dự đoán được giá của xe
- Tập dữ liệu này:
  - 205 mẫu trong tập dữ liệu
  - mỗi mẫu có 26 thuộc tính

|      | Tên thuộc tính    | Kiểu dữ liệu | Trung bình/ số giá trị phân biệt | Std/Isolated valuess | Số mẫu bị  thiếu |
| ---- | ----------------- | ------------ | -------------------------------- | -------------------- | ---------------- |
| 0    | symboling         | nominal      | 6                                | 0                    | 0 (0.00%)        |
| 1    | normalized-losses | numerical    | 122.00                           | 35.33                | 41 (20.00%)      |
| 2    | make              | nominal      | 22                               | 1                    | 0 (0.00%)        |
| 3    | fuel-type         | nominal      | 2                                | 0                    | 0 (0.00%)        |
| 4    | aspiration        | nominal      | 2                                | 0                    | 0 (0.00%)        |
| 5    | num-of-doors      | nominal      | 2                                | 0                    | 2 (0.98%)        |
| 6    | body-style        | nominal      | 5                                | 0                    | 0 (0.00%)        |
| 7    | drive-wheels      | nominal      | 3                                | 0                    | 0 (0.00%)        |
| 8    | engine-location   | nominal      | 2                                | 0                    | 0 (0.00%)        |
| 9    | wheel-base        | numerical    | 98.76                            | 6.01                 | 0 (0.00%)        |
| 10   | length            | numerical    | 174.05                           | 12.31                | 0 (0.00%)        |
| 11   | width             | numerical    | 65.91                            | 2.14                 | 0 (0.00%)        |
| 12   | height            | numerical    | 53.72                            | 2.44                 | 0 (0.00%)        |
| 13   | curb-weight       | numerical    | 2555.57                          | 519.41               | 0 (0.00%)        |
| 14   | engine-type       | nominal      | 7                                | 1                    | 0 (0.00%)        |
| 15   | num-of-cylinders  | nominal      | 7                                | 2                    | 0 (0.00%)        |
| 16   | engine-size       | numerical    | 126.91                           | 41.54                | 0 (0.00%)        |
| 17   | fuel-system       | nominal      | 8                                | 2                    | 0 (0.00%)        |
| 18   | bore              | numerical    | 3.33                             | 0.27                 | 4 (1.95%)        |
| 19   | stroke            | numerical    | 3.26                             | 0.32                 | 4 (1.95%)        |
| 20   | compression-ratio | numerical    | 10.14                            | 3.96                 | 0 (0.00%)        |
| 21   | horsepower        | numerical    | 104.26                           | 39.62                | 2 (0.98%)        |
| 22   | peak-rpm          | numerical    | 5125.37                          | 478.15               | 2 (0.98%)        |
| 23   | city-mpg          | numerical    | 25.22                            | 6.53                 | 0 (0.00%)        |
| 24   | highway-mpg       | numerical    | 30.75                            | 6.87                 | 0 (0.00%)        |
| 25   | price             | numerical    | 13207.13                         | 7927.27              | 4 (1.95%)        |

### Tập dữ liệu 2

- Tập dữ liệu được thu thập về thông tin của các mảnh vỡ kim loại về các thuộc tính của chúng, từ thông tin này chúng ta có thể dự đoán được các mảnh vỡ này có phải là 1 phần của 1 ống đồng nối dài hay không.
- Tập dữ liệu này:
  - có 512 mẫu trong tập dữ liệu
  - mỗi mẫu có 40 thuộc tính

|      | Tên thuộc tính      | Kiểu dữ liệu | Trung bình/ số giá trị phân biệt | Phương sai/số giá trị duy nhất | Số mẫu bị  thiếu |
| ---- | ------------------- | ------------ | -------------------------------- | ------------------------------ | ---------------- |
| 0    | timestamp           | nominal      | 297                              | 162                            | 0 (0.00%)        |
| 1    | cylinder-number     | nominal      | 434                              | 350                            | 1 (0.18%)        |
| 2    | customer            | nominal      | 84                               | 19                             | 0 (0.00%)        |
| 3    | job-number          | nominal      | 262                              | 117                            | 1 (0.18%)        |
| 4    | grain-screened      | nominal      | 3                                | 1                              | 49 (9.06%)       |
| 5    | ink-color           | nominal      | 4                                | 1                              | 0 (0.00%)        |
| 6    | proof-on-ctd-ink    | nominal      | 3                                | 1                              | 57 (10.54%)      |
| 7    | blade-mfg           | nominal      | 3                                | 2                              | 60 (11.09%)      |
| 8    | cylinder-division   | nominal      | 3                                | 1                              | 0 (0.00%)        |
| 9    | paper-type          | nominal      | 6                                | 1                              | 0 (0.00%)        |
| 10   | ink-type            | nominal      | 6                                | 0                              | 1 (0.18%)        |
| 11   | direct-steam        | nominal      | 4                                | 1                              | 25 (4.62%)       |
| 12   | solvent-type        | nominal      | 3                                | 0                              | 56 (10.35%)      |
| 13   | type-on-cylinder    | nominal      | 4                                | 0                              | 19 (3.51%)       |
| 14   | press-type          | nominal      | 4                                | 0                              | 1 (0.18%)        |
| 15   | press               | nominal      | 8                                | 0                              | 1 (0.18%)        |
| 16   | unit-number         | nominal      | 8                                | 1                              | 0 (0.00%)        |
| 17   | cylinder-size       | nominal      | 8                                | 2                              | 3 (0.55%)        |
| 18   | paper-mill-location | nominal      | 7                                | 2                              | 156 (28.84%)     |
| 19   | plating-tank        | nominal      | 4                                | 2                              | 18 (3.33%)       |
| 20   | proof-cut           | numerical    | 45.17                            | 9.48                           | 54 (9.98%)       |
| 21   | viscosity           | numerical    | 51.03                            | 8.27                           | 5 (0.92%)        |
| 22   | caliper             | numerical    | 0.28                             | 0.07                           | 27 (4.99%)       |
| 23   | ink-temperature     | numerical    | 15.36                            | 1.28                           | 2 (0.37%)        |
| 24   | humifity            | numerical    | 78.54                            | 7.73                           | 1 (0.18%)        |
| 25   | roughness           | numerical    | 0.72                             | 0.19                           | 30 (5.55%)       |
| 26   | blade-pressure      | numerical    | 30.91                            | 9.11                           | 63 (11.65%)      |
| 27   | varnish-pct         | numerical    | 5.78                             | 6.84                           | 55 (10.17%)      |
| 28   | press-speed         | numerical    | 1823.36                          | 328.40                         | 10 (1.85%)       |
| 29   | ink-pct             | numerical    | 55.64                            | 5.56                           | 55 (10.17%)      |
| 30   | solvent-pct         | numerical    | 38.57                            | 3.50                           | 55 (10.17%)      |
| 31   | ESA-Voltage         | numerical    | 1.32                             | 2.46                           | 56 (10.35%)      |
| 32   | ESA-Amperage        | numerical    | 0.04                             | 0.42                           | 54 (9.98%)       |
| 33   | wax                 | numerical    | 2.40                             | 0.55                           | 6 (1.11%)        |
| 34   | hardener            | numerical    | 0.99                             | 0.37                           | 7 (1.29%)        |
| 35   | roller-durometer    | numerical    | 34.78                            | 4.50                           | 54 (9.98%)       |
| 36   | current-density     | numerical    | 39.06                            | 2.35                           | 7 (1.29%)        |
| 37   | anode-space-ratio   | numerical    | 103.03                           | 5.00                           | 7 (1.29%)        |
| 38   | chrome-content      | numerical    | 99.60                            | 1.85                           | 3 (0.55%)        |
| 39   | band-type           | nominal      | 3                                | 0                              | 0 (0.00%)        |