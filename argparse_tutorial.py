import argparse
import os

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='Argparse Tutorial')

# 입력받을 인자값 설정 (default 값 설정가능)
parser.add_argument('--save_dir', type=str, default='save_dir')
parser.add_argument('--time', type=int, default=30)

# args 에 위의 내용 저장
args    = parser.parse_args()

os.mkdir(args.save_dir)

# 입력받은 인자값 출력
print(args.save_dir)
print(args.time)