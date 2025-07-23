# CBRapi
## Сервис имитирует работу официального API ЦБ РФ, возвращая случайные значения курсов валют в заданных диапазонах.


### Запуск

```bash
# Клонировать репозиторий
git clone https://github.com/malindev07/CBRapi.git
cd CBRapi

# Установить зависимости и запустить сервис
make run
```

## Что возвращает сервис

Если дата валидна сервис возвращает XML-документ со следующими данными:
status_code = 200
```xml
<ValCurs Date="01/01/2022" name="Foreign Currency Market">
  <Valute ID="R01010">
    <NumCode>036</NumCode>
    <CharCode>AUD</CharCode>
    <Nominal>1</Nominal>
    <Name>Австралийский доллар</Name>
    <Value>59,039</Value>
    <VunitRate>59.039</VunitRate>
  </Valute>
  <Valute ID="R01020A">
    <NumCode>944</NumCode>
    <CharCode>AZN</CharCode>
    <Nominal>1</Nominal>
    <Name>Азербайджанский манат</Name>
    <Value>58,5063</Value>
    <VunitRate>58.5063</VunitRate>
  </Valute>
</ValCurs>
```
Если дата невалидна сервис возвращает:
status_code = 500
```xml
<ValCurs> Error in parameters </ValCurs>
```
