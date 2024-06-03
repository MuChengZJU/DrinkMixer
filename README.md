# 求是创新奶茶店

## 简介

欢迎来到是创新奶茶店！这是一个使用Pygame构建的饮料混合模拟游戏。在游戏中，玩家需要根据客户的订单混合不同的饮料成分以满足客户的需求。

## 文件结构

```plaintext
drink_mixer_game/
├── assets/
│   ├── images/
│   │   ├── base_coffee.png
│   │   ├── base_soda.png
│   │   ├── flavor_fruit.png
│   │   ├── flavor_gel.png
│   │   ├── flavor_mint.png
│   │   ├── extra_milk.png
│   │   ├── extra_tomato.png
│   │   ├── mixing_cup.png
│   │   └── redo_button.png
│   └── sounds/
├── customer.py
├── display.py
├── game.py
├── glass.py
├── main.py
├── requirements.txt
└── setup.py
```

## 安装与运行

### 前置条件

- Python 3.x
- Pygame

### 安装步骤

1. 克隆该仓库到本地:
    ```sh
    git clone https://github.com/yourusername/drink_mixer_game.git
    cd drink_mixer_game
    ```

2. 创建并激活虚拟环境（可选但推荐）:
    ```sh
    python -m venv venv
    source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
    ```

3. 安装依赖项:
    ```sh
    pip install -r requirements.txt
    ```

4. 运行游戏:
    ```sh
    python main.py
    ```

## 游戏玩法

- 启动游戏后，玩家将看到一个包含各种饮料成分的界面。
- 客户的订单会显示在屏幕上方，玩家需要根据订单选择合适的饮料成分。
- 点击相应的饮料成分图标将其添加到杯中。
- 点击“重做这杯”按钮可以清空当前杯子里的内容。
- 当完成混合后，点击“混合杯”按钮来检查订单是否正确。如果正确，游戏会增加相应的收入，否则会扣掉一定的积分。
- 点击“退出游戏”按钮来退出游戏。

## 文件说明

- `main.py`: 游戏的入口文件，初始化Pygame并启动游戏循环。
- `game.py`: 包含游戏逻辑和主循环。
- `display.py`: 负责绘制游戏界面和处理用户交互。
- `glass.py`: 模拟饮料杯，包含添加成分和清空杯子的方法。
- `customer.py`: 生成客户和订单。
- `sound.py`: 处理游戏中的音效和背景音乐。
- `setup.py`: 用于打包游戏的配置文件。
- `requirements.txt`: 包含游戏所需的Python依赖项。
- `assets/`: 存放游戏所需的图像和音效文件。

## 贡献

如果您有任何改进建议或发现了bug，欢迎提交issue或pull request。

## 许可

本项目采用MIT许可证。

---

感谢您的参与和支持！希望您在游戏中玩得愉快！