import java.time.*;
import java.time.DayOfWeek;

class Main {
	public static void main(String[] args)
	{
		LocalDate localDate = LocalDate.of(2002,02,04);
		System.out.println(localDate);
		DayOfWeek dayOfWeek = DayOfWeek.from(localDate);
		System.out.println(dayOfWeek.name());
	}
}
