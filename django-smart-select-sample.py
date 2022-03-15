from smart_selects.db_fields import ChainedForeignKey 



Continent(models.Model):
    name = models.CharField()

Country(models.Model):
    name = models.CharField()
    continent = models.ForeignKey(Continent)
    
    
Location(models.Model):
    newcontinent = models.ForeignKey(Continent) 
    newcountry = ChainedForeignKey(
        Country, # the model where you're populating your countries from
        chained_field="newcontinent", # the field on your own model that this field links to 
        chained_model_field="continent", # the field on Country that corresponds to newcontinent
        show_all=False, # only shows the countries that correspond to the selected continent in newcontinent
    )
