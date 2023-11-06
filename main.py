"""
infection

Description:
"""
# import tsk
import random
import pygame

pygame.init()

# create the window
w = pygame.display.set_mode([1000, 500])

# Create the players
p1 = pygame.Rect(400, 250, 20, 20)
p2 = pygame.Rect(500, 250, 20, 20)
p3 = pygame.Rect(600, 250, 20, 20)

# Create the variables
run = True
it = 0
p1m = True
p2m = True
p3m = True
p1color = (255, 255, 255)
p2color = (255, 255, 255)
p3color = (255, 255, 255)
itcolor = (0, 255, 0)
p2it = False
p3it = False
p1it = False

# Set the IT
who = random.randint(1, 3)
if who == 1:
    p1it = True
    p1color = itcolor
if who == 2:
    p2it = True
    p2color = itcolor
if who == 3:
    p3it = True
    p3color = itcolor


# # Move Player
# def p1_move():
#     global p1
#     global p1m
#     if p1m == True:
#         if tsk.get_key_pressed(pygame.K_w):
#             p1.y -= 3
#         if tsk.get_key_pressed(pygame.K_s):
#             p1.y += 3
#         if tsk.get_key_pressed(pygame.K_a):
#             p1.x -= 3
#         if tsk.get_key_pressed(pygame.K_d):
#             p1.x += 3
#
#
# def p2_move():
#     global p2
#     global p2m
#     if p2m == True:
#         if tsk.get_key_pressed(pygame.K_i):
#             p2.y -= 3
#         if tsk.get_key_pressed(pygame.K_k):
#             p2.y += 3
#         if tsk.get_key_pressed(pygame.K_j):
#             p2.x -= 3
#         if tsk.get_key_pressed(pygame.K_l):
#             p2.x += 3
#
#
# def p3_move():
#     global p3
#     global p3m
#     if p3m == True:
#         if tsk.get_key_pressed(pygame.K_UP):
#             p3.y -= 3
#         if tsk.get_key_pressed(pygame.K_DOWN):
#             p3.y += 3
#         if tsk.get_key_pressed(pygame.K_LEFT):
#             p3.x -= 3
#         if tsk.get_key_pressed(pygame.K_RIGHT):
#             p3.x += 3


# Game Intro
print(
    'Welcome to Infection! A random player gets to be the "infected" and infect everyone! Good luck not getting infected :)')

# Game loop
while run:
    w.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        p3.y -= 1
    if keys[pygame.K_DOWN]:
        p3.y += 1
    if keys[pygame.K_LEFT]:
        p3.x -= 1
    if keys[pygame.K_RIGHT]:
        p3.x += 1

    if keys[pygame.K_w]:
        p1.y -= 1
    if keys[pygame.K_s]:
        p1.y += 1
    if keys[pygame.K_a]:
        p1.x -= 1
    if keys[pygame.K_d]:
        p1.x += 1

    if keys[pygame.K_i]:
        p2.y -= 1
    if keys[pygame.K_k]:
        p2.y += 1
    if keys[pygame.K_j]:
        p2.x -= 1
    if keys[pygame.K_l]:
        p2.x += 1

    # Players movement
    # p1_move()
    # p2_move()
    # p3_move()

    # Draw the players
    pygame.draw.rect(w, p1color, p1)
    pygame.draw.rect(w, p2color, p2)
    pygame.draw.rect(w, p3color, p3)

    # Players border
    if p1.x < 0:
        p1.x = 0
    if p1.x >= 980:
        p1.x = 980
    if p1.y < 0:
        p1.y = 0
    if p1.y > 480:
        p1.y = 480

    if p2.x < 0:
        p2.x = 0
    if p2.x > 980:
        p2.x = 980
    if p2.y < 0:
        p2.y = 0
    if p2.y > 480:
        p2.y = 480

    if p3.x < 0:
        p3.x = 0
    if p3.x > 980:
        p3.x = 980
    if p3.y < 0:
        p3.y = 0
    if p3.y > 480:
        p3.y = 480

    if p1.colliderect(p2):
        if p1it == True:
            p2it = True
            p2color = itcolor
        if p2it == True:
            p1it = True
            p1color = itcolor

    if p1.colliderect(p3):
        if p1it == True:
            p3it = True
            p3color = itcolor

        if p3it == True:
            p1it = True
            p1color = itcolor

    if p2.colliderect(p3):
        if p2it == True:
            p3it = True
            p3color = itcolor

        if p3it == True:
            p2it = True
            p2color = itcolor

    if p2it == True and p3it == True and p1it == True:
        print()
        print("You have infected everyone! Tks for playing! :)")
        run = False

    # Flip the display
    pygame.display.flip()