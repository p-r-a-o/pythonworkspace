import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 680  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("prao Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/prao/Desktop/DEV.PRAO/pythonworkspace/pygame_basic/background.jpg")

# 이벤트 루프
running = True  # 게임이 진행 중인지 확인
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행 중이 아님

    # screen.fill((70,60,25)) # (R, G, B) 값으로 배경 설정
    screen.blit(background, (0, 0))  # 배경 그리기

    pygame.display.update() # 게임 화면을 다시 그리기
# pygame 종료
pygame.quit()
