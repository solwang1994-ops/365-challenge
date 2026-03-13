def show_menu():
    """显示菜单"""
    print("\n" + "="*30)
    print("📝 简易待办事项列表 (To-Do List)")
    print("="*30)
    print("1. 查看所有任务")
    print("2. 添加新任务")
    print("3. 删除任务")
    print("4. 退出程序")
    print("="*30)

def view_tasks(tasks):
    """查看任务列表"""
    if not tasks:
        print("\n💤 目前没有任何任务，快去添加一个吧！")
    else:
        print("\n📋 当前任务列表:")
        # enumerate 可以同时获取索引(i)和内容(task)，start=1 让编号从1开始
        for i, task in enumerate(tasks, start=1):
            print(f"   [{i}] {task}")

def add_task(tasks):
    """添加任务"""
    task = input("\n✨ 请输入新任务内容: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ 成功添加: '{task}'")
    else:
        print("⚠️ 任务内容不能为空！")

def delete_task(tasks):
    """删除任务"""
    view_tasks(tasks) # 先展示一下，方便用户看编号
    
    if not tasks:
        return # 如果没任务，直接返回，不执行后面逻辑

    try:
        choice = input("\n🗑️ 请输入要删除的任务编号: ")
        index = int(choice) - 1 # 用户输入的是1,2,3，列表索引是0,1,2
        
        # 检查索引是否在合法范围内
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"🗑️ 已删除: '{removed_task}'")
        else:
            print("❌ 错误：编号不存在，请检查输入。")
            
    except ValueError:
        print("❌ 错误：请输入有效的数字编号！")

def main():
    # 1. 初始化数据容器 (列表)
    todo_list = []
    
    print("👋 欢迎使用 To-Do List 管理器！")
    
    while True:
        show_menu()
        choice = input("请选择操作 (1-4): ").strip()
        
        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            delete_task(todo_list)
        elif choice == '4':
            print("\n👋 再见！祝你今天效率满满！")
            break # 跳出循环，结束程序
        else:
            print("⚠️ 无效的选择，请输入 1 到 4 之间的数字。")

# 只有当这个文件被直接运行时，才执行 main()
if __name__ == "__main__":
    main()