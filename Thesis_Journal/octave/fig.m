ROWS = 120;
COLS = 80;
BLACK = 0;
WHITE = 255;
GRAY = WHITE/2;

A = WHITE * ones(ROWS, COLS);

function[A] = hline(A, i,j, len, color)
	for y=j:j+len
		if mod(i,2) == 0 && mod(y,2) == 0
			A(i,j) = color;
		end
	end
end

%function[] = vertical(i,j, len, color)
%	A(i:i+len,j) = color;
%end



r = 10;
p_x = 50; 
p_y = 50;
for i=1:ROWS
	for j=1:COLS
		if 1==1
		if (p_y-i)^2 + (p_x-j)^2 < r^2
			continue ;
		end
		end
		if mod(i,2) == 0 && mod (j,2) == 0
			A(i,j) = GRAY;
		end
	end
end


%for i=1:ROWS
%	for j=1:COLS
%		A = hline(A,i,j,COLS-i,BLACK);
%	end
%end

if (1==1)
A(15:50,30:60) = WHITE;
A(50:60,45:60) = WHITE;
A(60:80,30:60) = WHITE;

for i=20:80
	if mod(i,2) == 0
	A(i,60) = BLACK;
	end
end

for i=30:60
	if mod(i,2) == 0
	A(80,i) = BLACK;
	end
end

for i=30:45
	if mod(i,2) == 0
	A(60,i) = BLACK;
	end
end


for i=60:80
	if mod(i,2) == 0
	A(i,30) = BLACK;
	end
end

A(16,56) = GRAY;
A(16,58) = GRAY;
A(16,60) = GRAY;
A(18,58) = GRAY;
A(18,60) = GRAY;
A(18,60) = GRAY;
A(20,60) = GRAY;
end

%A(50:60,45) = BLACK;

for i=1:ROWS
	for j=1:COLS
		if (30-i)^2 + (30-j)^2 <= 20^2
			if mod(i,2) == 0 && mod (j,2) == 0
				A(i,j) = WHITE;
			end
		end	

		if (30-i)^2 + (30-j)^2 == 20^2
			A(i,j) = BLACK;
		end
	end
end

imshow(A / 255);
