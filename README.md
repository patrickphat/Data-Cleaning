## Thông tin nhóm

Nhóm 8

Nguyễn Trường Phát `17520880`

Nguyễn Chí Bảo `17520271`

## Dữ liệu

- Nằm ở 3 thư mục `dataset-1`, `dataset-2` và `dataset-3` 
- Mỗi thư mục chứa 3 file dữ liệu tên `load.data`, một file ghi kiểu thuộc tính `attributes.txt` và 1 file mô tả tên là `info.txt`

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

### Tập dữ liệu 3

- Tập dữ liệu được thu thập về thông tin của về các xét nghiệm của khối u ở ngực của các nữ bệnh nhân, từ thông tin này chúng ta có thể dự đoán khối u này có lành tính (benign) hay ác tính (malignant) không.
- Tập dữ liệu này:
  - có mẫu 699  trong tập dữ liệu
  - mỗi mẫu có 10 thuộc tính

|      | Tên thuộc tính              | Kiểu dữ liệu | Trung bình/ số giá trị phân biệt | Phương sai/số giá trị duy nhất | Số mẫu bị  thiếu |
| ---- | --------------------------- | ------------ | -------------------------------- | ------------------------------ | ---------------- |
| 0    | Sample-code-number          | nominal      | 645                              | 599                            | 0 (0.00%)        |
| 1    | Clump-Thickness             | numerical    | 4.42                             | 2.81                           | 0 (0.00%)        |
| 2    | Uniformity-of-Cell-Size     | numerical    | 3.13                             | 3.05                           | 0 (0.00%)        |
| 3    | Uniformity-of-Cell-Shape    | numerical    | 3.21                             | 2.97                           | 0 (0.00%)        |
| 4    | Marginal-Adhesion           | numerical    | 2.81                             | 2.85                           | 0 (0.00%)        |
| 5    | Single-Epithelial-Cell-Size | numerical    | 3.22                             | 2.21                           | 0 (0.00%)        |
| 6    | Bare-Nuclei                 | numerical    | 3.54                             | 3.64                           | 16 (2.29%)       |
| 7    | Bland-Chromatin             | numerical    | 3.44                             | 2.44                           | 0 (0.00%)        |
| 8    | Normal-Nucleoli             | numerical    | 2.87                             | 3.05                           | 0 (0.00%)        |
| 9    | Mitoses                     | numerical    | 1.59                             | 1.71                           | 0 (0.00%)        |
| 10   | Class                       | nominal      | 2                                | 0                              | 0 (0.00%)        |

## Bài tập 2 - Xử lý dữ liệu

Xây dựng một chương trình với câu lệnh chạy có dạng:

```bash
python data_processing.py --option <option> --input <input_folder> --output <output_file> --log <log_file>
```

Ví dụ: 

```bash 
python data_processing.py --option summary --input /dataset-1 --output output.xlsx --log log.txt 
```

Trong đó:
`--option` Cho biết các thao tác cần thực hiện. Chi tiết mã tùy chọn được
ghi trong từng chức năng cụ thể.
`--input` Đường dẫn **thư mục** chứa dữ liệu đầu vào. Gồm tập tin chứa dữ liệu `load.data` và loại dữ liệu ứng với từng data `attributes.txt`
`--output`: Đường dẫn tập tin đầu ra chứa dữ liệu sau khi xử lý. Định
dạng được mô tả bên dưới.
`--log` Tập tin chứa các thông tin đã xử lý. Nội dung chi tiết được
mô tả chi tiết trong từng chức năng.

#### option: Summary

Chức năng chính: Tóm tắt dữ liệu

```bash
python data_processing.py --option summary --input <input_folder> --log <log_file>
```

`--option`= summary
`--log`: đường dẫn tới file ghi lại các thông tin về số mẫu, số thuộc tính, liệt kê tên các thuộc tính và kiểu dữ liệu tương ứng (numeric/nominal)

Nếu `--log` không được khai báo, tập tin log sẽ được mặc định lưu tại `<input_folder>/summary_log.txt`

#### option: Replace 

Chức năng chính: Thay thế những chỗ bị thiếu dữ liệu

```bash
python data_processing.py --option summary --input <input_folder> --output <output_file> --log <log_file>
```

`--option`= replace

`--output`: đường dẫn tới file sau khi đã được xử lý. Định dạng file nên là `.data` hoặc `.csv`

`--log`: đường dẫn tới file ghi cụ thể thuộc tính thiếu, số giá trị thiếu và giá trị mới dùng để thay thế. Cụ thể:

```
# thuộc tính: <tên thuộc tính>, <số giá trị thiếu>, <giá trị mới>
...
```

Nếu `--log` không được khai báo, tập tin log sẽ được mặc định lưu tại `<input_folder>/replace_log.txt`

Nếu `--output` không được khai báo, tập tin log sẽ được mặc định lưu tại `<input_folder>/replace_output.csv`

