# 单元测试覆盖率报告生成步骤：
# 运行 run_all_unit_test.sh
# 再使用 coverage combine 命令合并报告
# 使用 coverage report --omit="test_*.py" -m 命令行直接查看报告
# 使用 coverage html --omit="test_*.py" 生成html页面报告
# --omit="test_*.py" 为忽略测试用例模块自身的覆盖率，只查看功能模块的测试覆盖率情况

[[ -d "advisor" ]] || ln -s ../advisor advisor

for file in $(ls test*.py); do
    coverage run -p --omit="test_*.py" "$file"
done
coverage combine
coverage html
