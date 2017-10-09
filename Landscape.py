import sys, pygame, Perlin, math
pygame.init()

size = width, height = 800, 800

screen = pygame.display.set_mode(size)


#CONSTANTS
CHUNK_SIZE = 128
PIXEL_SIZE = 4

def getColor(height):
	if height <= 0.20:
		return (105,210,231)
	if height <= 0.34:
		return (167,219,216)
	if height <= 0.37:
		return (224,228,204)
	if height <= 0.4:
		return (186,219,129)
	if height <= 0.6:
		return (124,197,130)
	if height <= 0.68:
		return (62,175,131)
	if height <= 0.75:
		return (143,154,156)
	if height <= 0.8:
		return (190,195,188)
	if height <= 0.85:
		return (215,218,207)
	else:
		return (230,232,227)

def genChunk(x, y):
	surface = pygame.Surface((CHUNK_SIZE, CHUNK_SIZE))
	for i in range(CHUNK_SIZE // PIXEL_SIZE):
		for j in range(CHUNK_SIZE // PIXEL_SIZE):
			color = getColor(perlin.octave(i * PIXEL_SIZE + x * CHUNK_SIZE, j * PIXEL_SIZE + y * CHUNK_SIZE, 3, 0.5))
			for xOffset in range(PIXEL_SIZE):
				for yOffset in range(PIXEL_SIZE):
					surface.set_at((i * PIXEL_SIZE + xOffset, j * PIXEL_SIZE + yOffset), color)
	return surface

screen.fill((0, 0, 0))
screenX = 0
screenY = 0

perlin = Perlin.Perlin(350)
y = 0

surfaces = {}

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	inKeys = pygame.key.get_pressed()

	if inKeys[pygame.K_ESCAPE]:
		sys.exit()
	if inKeys[pygame.K_RIGHT]:
		screenX += 1
	if inKeys[pygame.K_LEFT]:
		screenX -= 1
	if inKeys[pygame.K_UP]:
		screenY -= 1
	if inKeys[pygame.K_DOWN]:
		screenY += 1

	chunkGenerated = False
	screen.fill((0, 0, 0))
	for x in range(screenX // CHUNK_SIZE, (width + screenX) // CHUNK_SIZE + 1):
		for y in range(screenY // CHUNK_SIZE, (height + screenY) // CHUNK_SIZE + 1):
			if (x, y) in surfaces:
				screen.blit(surfaces[x,y], (CHUNK_SIZE * x - screenX, CHUNK_SIZE * y - screenY))
			elif not chunkGenerated:
				chunkGenerated = True
				surfaces[x, y] = genChunk(x, y)

	pygame.display.flip()