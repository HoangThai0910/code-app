import os
import sys

def split_file(file_path, chunk_size=20*1024*1024):
    """Chia nhỏ file thành các phần có kích thước tối đa 20MB."""
    if not os.path.isfile(file_path):
        print("File không tồn tại.")
        return
    
    file_size = os.path.getsize(file_path)
    num_parts = (file_size // chunk_size) + (1 if file_size % chunk_size else 0)
    
    with open(file_path, 'rb') as f:
        for i in range(num_parts):
            part_filename = f"{file_path}.part{i}"
            with open(part_filename, 'wb') as part_file:
                part_file.write(f.read(chunk_size))
            print(f"Đã tạo: {part_filename}")

def merge_files(output_file, part_prefix):
    """Gộp các phần thành file .deb ban đầu."""
    part_files = sorted([f for f in os.listdir('.') if f.startswith(part_prefix)], key=lambda x: int(x.split('part')[-1]))
    
    if not part_files:
        print("Không tìm thấy các phần file.")
        return
    
    with open(output_file, 'wb') as output:
        for part_file in part_files:
            with open(part_file, 'rb') as pf:
                output.write(pf.read())
            print(f"Đã ghép: {part_file}")
    
    print(f"Hoàn tất gộp file: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py split/merge <file>")
        sys.exit(1)
    
    command = sys.argv[1]
    file_path = sys.argv[2]
    
    if command == "split":
        split_file(file_path)
    elif command == "merge":
        merge_files(file_path, file_path + ".part")
    else:
        print("Lệnh không hợp lệ, sử dụng split hoặc merge.")
