DAY=$1

if [ -z "$DAY" ]
  then
    echo "Usage: $(basename $0) <day>"
    exit 1
fi

. ./.env
mkdir "day$DAY"
cd day$DAY
curl -o input.txt --cookie "session=$AOC_SESSION" https://adventofcode.com/2020/day/$DAY/input
cd -
