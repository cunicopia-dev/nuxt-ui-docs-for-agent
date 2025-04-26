<!-- source: https://ui.nuxt.com/components/stepper --> # Stepper

[Stepper](https://reka-
ui.com/docs/components/stepper)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Stepper.vue)

A set of steps that are used to indicate progress through a multi-step
process.

## Usage

### Items

Use the `items` prop as an array of objects with the following properties:

  * `title?: string`
  * `description?: AvatarProps`
  * `content?: string`
  * `icon?: string`
  * `value?: string | number`
  * `disabled?: boolean`
  * `slot?: string`

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items = ref<StepperItem[]>([
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      },
      {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      },
      {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ])
    </script>
    
    <template>
      <UStepper :items="items" class="w-full" />
    </template>
    

Click on the items to navigate through the steps.

### Color

Use the `color` prop to change the color of the Stepper.

color

neutral

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items = ref<StepperItem[]>([
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      },
      {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      },
      {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ])
    </script>
    
    <template>
      <UStepper color="neutral" :items="items" class="w-full" />
    </template>
    

### Size

Use the `size` prop to change the size of the Stepper.

size

xl

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items = ref<StepperItem[]>([
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      },
      {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      },
      {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ])
    </script>
    
    <template>
      <UStepper size="xl" :items="items" class="w-full" />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the Stepper. Defaults
to `horizontal`.

orientation

vertical

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items = ref<StepperItem[]>([
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      },
      {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      },
      {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ])
    </script>
    
    <template>
      <UStepper orientation="vertical" :items="items" class="w-full" />
    </template>
    

### Disabled

Use the `disabled` prop to disable navigation through the steps.

disabled

true

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items = ref<StepperItem[]>([
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      },
      {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      },
      {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ])
    </script>
    
    <template>
      <UStepper disabled :items="items" />
    </template>
    

This can be useful when you want to force navigation with controls.

## Examples

### With controls

You can add additional controls for the stepper using buttons.

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

Address

Step 0 of 0

Prev  Next

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items: StepperItem[] = [
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      }, {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      }, {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ]
    
    const stepper = useTemplateRef('stepper')
    </script>
    
    <template>
      <div class="w-full">
        <UStepper ref="stepper" :items="items">
          <template #content="{ item }">
            <Placeholder class="aspect-video">
              {{ item.title }}
            </Placeholder>
          </template>
        </UStepper>
    
        <div class="flex gap-2 justify-between mt-4">
          <UButton
            leading-icon="i-lucide-arrow-left"
            :disabled="!stepper?.hasPrev"
            @click="stepper?.prev()"
          >
            Prev
          </UButton>
    
          <UButton
            trailing-icon="i-lucide-arrow-right"
            :disabled="!stepper?.hasNext"
            @click="stepper?.next()"
          >
            Next
          </UButton>
        </div>
      </div>
    </template>
    

### Control active item

You can control the active item by using the `default-value` prop or the
`v-model` directive with the index of the item.

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

This is the Address step.

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    import { onMounted, ref } from 'vue'
    
    const items: StepperItem[] = [
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      }, {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      }, {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ]
    
    const active = ref(0)
    
    // Note: This is for demonstration purposes only. Don't do this at home.
    onMounted(() => {
      setInterval(() => {
        active.value = (active.value + 1) % items.length
      }, 2000)
    })
    </script>
    
    <template>
      <UStepper v-model="active" :items="items" class="w-full">
        <template #content="{ item }">
          <Placeholder class="aspect-video">
            This is the {{ item?.title }} step.
          </Placeholder>
        </template>
      </UStepper>
    </template>
    

You can also pass the `value` of one of the items if provided.

### With content slot

Use the `#content` slot to customize the content of each item.

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

This is the Address step.

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items: StepperItem[] = [
      {
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      }, {
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      }, {
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ]
    </script>
    
    <template>
      <UStepper ref="stepper" :items="items" class="w-full">
        <template #content="{ item }">
          <Placeholder class="aspect-video">
            This is the {{ item?.title }} step.
          </Placeholder>
        </template>
      </UStepper>
    </template>
    

### With custom slot

Use the `slot` property to customize a specific item.

#### Address

Add your address here

#### Shipping

Set your preferred shipping method

3

#### Checkout

Confirm your order

Address

Step 0 of 0

    
    
    <script setup lang="ts">
    import type { StepperItem } from '@nuxt/ui'
    
    const items = [
      {
        slot: 'address' as const,
        title: 'Address',
        description: 'Add your address here',
        icon: 'i-lucide-house'
      }, {
        slot: 'shipping' as const,
        title: 'Shipping',
        description: 'Set your preferred shipping method',
        icon: 'i-lucide-truck'
      }, {
        slot: 'checkout' as const,
        title: 'Checkout',
        description: 'Confirm your order'
      }
    ] satisfies StepperItem[]
    </script>
    
    <template>
      <UStepper :items="items" class="w-full">
        <template #address>
          <Placeholder class="aspect-video">
            Address
          </Placeholder>
        </template>
    
        <template #shipping>
          <Placeholder class="aspect-video">
            Shipping
          </Placeholder>
        </template>
    
        <template #checkout>
          <Placeholder class="aspect-video">
            Checkout
          </Placeholder>
        </template>
      </UStepper>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`items`| | `StepperItem[]`Show properties

  * `slot?: string`
  * `value?: string | number`
  * `title?: string`
  * `description?: string`
  * `icon?: string`
  * `content?: string`
  * `disabled?: boolean`

  
`size`| `'md'`| ` "xs" | "sm" | "md" | "lg" | "xl"`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation of the stepper.  
`defaultValue`| | ` string | number`The value of the step that should be active when initially rendered. Use when you do not need to control the state of the steps.  
`disabled`| | `boolean`  
`linear`| `true`| `boolean`Whether or not the steps must be completed in
order.  
`modelValue`| | ` string | number`  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; item?: ClassNameValue; container?: ClassNameValue; trigger?: ClassNameValue; ... 6 more ...; content?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`indicator`| `{ item: StepperItem; }`  
`title`| `{ item: StepperItem; }`  
`description`| `{ item: StepperItem; }`  
`content`| `{ item: StepperItem; }`  
  
### Emits

Event |  Type   
---|---  
`next`| `[payload: StepperItem]`  
`prev`| `[payload: StepperItem]`  
`update:modelValue`| `[value: string | number | undefined]`  
  
### Expose

You can access the typed component instance using
[`useTemplateRef`](https://vuejs.org/api/composition-api-
helpers.html#usetemplateref).

    
    
    <script setup lang="ts">
    const stepper = useTemplateRef('stepper')
    </script>
    
    <template>
      <UStepper ref="stepper" />
    </template>
    

This will give you access to the following:

Name| Type  
---|---  
`next`| `() => void`  
`prev`| `() => void`  
`hasNext`| `Ref<boolean>`  
`hasPrev`| `Ref<boolean>`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        stepper: {
          slots: {
            root: 'flex gap-4',
            header: 'flex',
            item: 'group text-center relative w-full',
            container: 'relative',
            trigger: 'rounded-full font-medium text-center align-middle flex items-center justify-center font-semibold group-data-[state=completed]:text-inverted group-data-[state=active]:text-inverted text-muted bg-elevated focus-visible:outline-2 focus-visible:outline-offset-2',
            indicator: 'flex items-center justify-center size-full',
            icon: 'shrink-0',
            separator: 'absolute rounded-full group-data-[disabled]:opacity-75 bg-accented',
            wrapper: '',
            title: 'font-medium text-default',
            description: 'text-muted text-wrap',
            content: 'size-full'
          },
          variants: {
            orientation: {
              horizontal: {
                root: 'flex-col',
                container: 'flex justify-center',
                separator: 'top-[calc(50%-2px)] h-0.5',
                wrapper: 'mt-1'
              },
              vertical: {
                header: 'flex-col gap-4',
                item: 'flex text-start',
                separator: 'start-[calc(50%-1px)] -bottom-[10px] w-0.5'
              }
            },
            size: {
              xs: {
                trigger: 'size-6 text-xs',
                icon: 'size-3',
                title: 'text-xs',
                description: 'text-xs',
                wrapper: 'mt-1.5'
              },
              sm: {
                trigger: 'size-8 text-sm',
                icon: 'size-4',
                title: 'text-xs',
                description: 'text-xs',
                wrapper: 'mt-2'
              },
              md: {
                trigger: 'size-10 text-base',
                icon: 'size-5',
                title: 'text-sm',
                description: 'text-sm',
                wrapper: 'mt-2.5'
              },
              lg: {
                trigger: 'size-12 text-lg',
                icon: 'size-6',
                title: 'text-base',
                description: 'text-base',
                wrapper: 'mt-3'
              },
              xl: {
                trigger: 'size-14 text-xl',
                icon: 'size-7',
                title: 'text-lg',
                description: 'text-lg',
                wrapper: 'mt-3.5'
              }
            },
            color: {
              primary: {
                trigger: 'group-data-[state=completed]:bg-primary group-data-[state=active]:bg-primary focus-visible:outline-primary',
                separator: 'group-data-[state=completed]:bg-primary'
              },
              secondary: {
                trigger: 'group-data-[state=completed]:bg-secondary group-data-[state=active]:bg-secondary focus-visible:outline-secondary',
                separator: 'group-data-[state=completed]:bg-secondary'
              },
              success: {
                trigger: 'group-data-[state=completed]:bg-success group-data-[state=active]:bg-success focus-visible:outline-success',
                separator: 'group-data-[state=completed]:bg-success'
              },
              info: {
                trigger: 'group-data-[state=completed]:bg-info group-data-[state=active]:bg-info focus-visible:outline-info',
                separator: 'group-data-[state=completed]:bg-info'
              },
              warning: {
                trigger: 'group-data-[state=completed]:bg-warning group-data-[state=active]:bg-warning focus-visible:outline-warning',
                separator: 'group-data-[state=completed]:bg-warning'
              },
              error: {
                trigger: 'group-data-[state=completed]:bg-error group-data-[state=active]:bg-error focus-visible:outline-error',
                separator: 'group-data-[state=completed]:bg-error'
              },
              neutral: {
                trigger: 'group-data-[state=completed]:bg-inverted group-data-[state=active]:bg-inverted focus-visible:outline-inverted',
                separator: 'group-data-[state=completed]:bg-inverted'
              }
            }
          },
          compoundVariants: [
            {
              orientation: 'horizontal',
              size: 'xs',
              class: {
                separator: 'start-[calc(50%+16px)] end-[calc(-50%+16px)]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'sm',
              class: {
                separator: 'start-[calc(50%+20px)] end-[calc(-50%+20px)]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'md',
              class: {
                separator: 'start-[calc(50%+28px)] end-[calc(-50%+28px)]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'lg',
              class: {
                separator: 'start-[calc(50%+32px)] end-[calc(-50%+32px)]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'xl',
              class: {
                separator: 'start-[calc(50%+36px)] end-[calc(-50%+36px)]'
              }
            },
            {
              orientation: 'vertical',
              size: 'xs',
              class: {
                separator: 'top-[30px]',
                item: 'gap-1.5'
              }
            },
            {
              orientation: 'vertical',
              size: 'sm',
              class: {
                separator: 'top-[38px]',
                item: 'gap-2'
              }
            },
            {
              orientation: 'vertical',
              size: 'md',
              class: {
                separator: 'top-[46px]',
                item: 'gap-2.5'
              }
            },
            {
              orientation: 'vertical',
              size: 'lg',
              class: {
                separator: 'top-[54px]',
                item: 'gap-3'
              }
            },
            {
              orientation: 'vertical',
              size: 'xl',
              class: {
                separator: 'top-[62px]',
                item: 'gap-3.5'
              }
            }
          ],
          defaultVariants: {
            size: 'md',
            color: 'primary'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            stepper: {
              slots: {
                root: 'flex gap-4',
                header: 'flex',
                item: 'group text-center relative w-full',
                container: 'relative',
                trigger: 'rounded-full font-medium text-center align-middle flex items-center justify-center font-semibold group-data-[state=completed]:text-inverted group-data-[state=active]:text-inverted text-muted bg-elevated focus-visible:outline-2 focus-visible:outline-offset-2',
                indicator: 'flex items-center justify-center size-full',
                icon: 'shrink-0',
                separator: 'absolute rounded-full group-data-[disabled]:opacity-75 bg-accented',
                wrapper: '',
                title: 'font-medium text-default',
                description: 'text-muted text-wrap',
                content: 'size-full'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'flex-col',
                    container: 'flex justify-center',
                    separator: 'top-[calc(50%-2px)] h-0.5',
                    wrapper: 'mt-1'
                  },
                  vertical: {
                    header: 'flex-col gap-4',
                    item: 'flex text-start',
                    separator: 'start-[calc(50%-1px)] -bottom-[10px] w-0.5'
                  }
                },
                size: {
                  xs: {
                    trigger: 'size-6 text-xs',
                    icon: 'size-3',
                    title: 'text-xs',
                    description: 'text-xs',
                    wrapper: 'mt-1.5'
                  },
                  sm: {
                    trigger: 'size-8 text-sm',
                    icon: 'size-4',
                    title: 'text-xs',
                    description: 'text-xs',
                    wrapper: 'mt-2'
                  },
                  md: {
                    trigger: 'size-10 text-base',
                    icon: 'size-5',
                    title: 'text-sm',
                    description: 'text-sm',
                    wrapper: 'mt-2.5'
                  },
                  lg: {
                    trigger: 'size-12 text-lg',
                    icon: 'size-6',
                    title: 'text-base',
                    description: 'text-base',
                    wrapper: 'mt-3'
                  },
                  xl: {
                    trigger: 'size-14 text-xl',
                    icon: 'size-7',
                    title: 'text-lg',
                    description: 'text-lg',
                    wrapper: 'mt-3.5'
                  }
                },
                color: {
                  primary: {
                    trigger: 'group-data-[state=completed]:bg-primary group-data-[state=active]:bg-primary focus-visible:outline-primary',
                    separator: 'group-data-[state=completed]:bg-primary'
                  },
                  secondary: {
                    trigger: 'group-data-[state=completed]:bg-secondary group-data-[state=active]:bg-secondary focus-visible:outline-secondary',
                    separator: 'group-data-[state=completed]:bg-secondary'
                  },
                  success: {
                    trigger: 'group-data-[state=completed]:bg-success group-data-[state=active]:bg-success focus-visible:outline-success',
                    separator: 'group-data-[state=completed]:bg-success'
                  },
                  info: {
                    trigger: 'group-data-[state=completed]:bg-info group-data-[state=active]:bg-info focus-visible:outline-info',
                    separator: 'group-data-[state=completed]:bg-info'
                  },
                  warning: {
                    trigger: 'group-data-[state=completed]:bg-warning group-data-[state=active]:bg-warning focus-visible:outline-warning',
                    separator: 'group-data-[state=completed]:bg-warning'
                  },
                  error: {
                    trigger: 'group-data-[state=completed]:bg-error group-data-[state=active]:bg-error focus-visible:outline-error',
                    separator: 'group-data-[state=completed]:bg-error'
                  },
                  neutral: {
                    trigger: 'group-data-[state=completed]:bg-inverted group-data-[state=active]:bg-inverted focus-visible:outline-inverted',
                    separator: 'group-data-[state=completed]:bg-inverted'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: {
                    separator: 'start-[calc(50%+16px)] end-[calc(-50%+16px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: {
                    separator: 'start-[calc(50%+20px)] end-[calc(-50%+20px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: {
                    separator: 'start-[calc(50%+28px)] end-[calc(-50%+28px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: {
                    separator: 'start-[calc(50%+32px)] end-[calc(-50%+32px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: {
                    separator: 'start-[calc(50%+36px)] end-[calc(-50%+36px)]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: {
                    separator: 'top-[30px]',
                    item: 'gap-1.5'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: {
                    separator: 'top-[38px]',
                    item: 'gap-2'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: {
                    separator: 'top-[46px]',
                    item: 'gap-2.5'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: {
                    separator: 'top-[54px]',
                    item: 'gap-3'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: {
                    separator: 'top-[62px]',
                    item: 'gap-3.5'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            stepper: {
              slots: {
                root: 'flex gap-4',
                header: 'flex',
                item: 'group text-center relative w-full',
                container: 'relative',
                trigger: 'rounded-full font-medium text-center align-middle flex items-center justify-center font-semibold group-data-[state=completed]:text-inverted group-data-[state=active]:text-inverted text-muted bg-elevated focus-visible:outline-2 focus-visible:outline-offset-2',
                indicator: 'flex items-center justify-center size-full',
                icon: 'shrink-0',
                separator: 'absolute rounded-full group-data-[disabled]:opacity-75 bg-accented',
                wrapper: '',
                title: 'font-medium text-default',
                description: 'text-muted text-wrap',
                content: 'size-full'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'flex-col',
                    container: 'flex justify-center',
                    separator: 'top-[calc(50%-2px)] h-0.5',
                    wrapper: 'mt-1'
                  },
                  vertical: {
                    header: 'flex-col gap-4',
                    item: 'flex text-start',
                    separator: 'start-[calc(50%-1px)] -bottom-[10px] w-0.5'
                  }
                },
                size: {
                  xs: {
                    trigger: 'size-6 text-xs',
                    icon: 'size-3',
                    title: 'text-xs',
                    description: 'text-xs',
                    wrapper: 'mt-1.5'
                  },
                  sm: {
                    trigger: 'size-8 text-sm',
                    icon: 'size-4',
                    title: 'text-xs',
                    description: 'text-xs',
                    wrapper: 'mt-2'
                  },
                  md: {
                    trigger: 'size-10 text-base',
                    icon: 'size-5',
                    title: 'text-sm',
                    description: 'text-sm',
                    wrapper: 'mt-2.5'
                  },
                  lg: {
                    trigger: 'size-12 text-lg',
                    icon: 'size-6',
                    title: 'text-base',
                    description: 'text-base',
                    wrapper: 'mt-3'
                  },
                  xl: {
                    trigger: 'size-14 text-xl',
                    icon: 'size-7',
                    title: 'text-lg',
                    description: 'text-lg',
                    wrapper: 'mt-3.5'
                  }
                },
                color: {
                  primary: {
                    trigger: 'group-data-[state=completed]:bg-primary group-data-[state=active]:bg-primary focus-visible:outline-primary',
                    separator: 'group-data-[state=completed]:bg-primary'
                  },
                  secondary: {
                    trigger: 'group-data-[state=completed]:bg-secondary group-data-[state=active]:bg-secondary focus-visible:outline-secondary',
                    separator: 'group-data-[state=completed]:bg-secondary'
                  },
                  success: {
                    trigger: 'group-data-[state=completed]:bg-success group-data-[state=active]:bg-success focus-visible:outline-success',
                    separator: 'group-data-[state=completed]:bg-success'
                  },
                  info: {
                    trigger: 'group-data-[state=completed]:bg-info group-data-[state=active]:bg-info focus-visible:outline-info',
                    separator: 'group-data-[state=completed]:bg-info'
                  },
                  warning: {
                    trigger: 'group-data-[state=completed]:bg-warning group-data-[state=active]:bg-warning focus-visible:outline-warning',
                    separator: 'group-data-[state=completed]:bg-warning'
                  },
                  error: {
                    trigger: 'group-data-[state=completed]:bg-error group-data-[state=active]:bg-error focus-visible:outline-error',
                    separator: 'group-data-[state=completed]:bg-error'
                  },
                  neutral: {
                    trigger: 'group-data-[state=completed]:bg-inverted group-data-[state=active]:bg-inverted focus-visible:outline-inverted',
                    separator: 'group-data-[state=completed]:bg-inverted'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: {
                    separator: 'start-[calc(50%+16px)] end-[calc(-50%+16px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: {
                    separator: 'start-[calc(50%+20px)] end-[calc(-50%+20px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: {
                    separator: 'start-[calc(50%+28px)] end-[calc(-50%+28px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: {
                    separator: 'start-[calc(50%+32px)] end-[calc(-50%+32px)]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: {
                    separator: 'start-[calc(50%+36px)] end-[calc(-50%+36px)]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: {
                    separator: 'top-[30px]',
                    item: 'gap-1.5'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: {
                    separator: 'top-[38px]',
                    item: 'gap-2'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: {
                    separator: 'top-[46px]',
                    item: 'gap-2.5'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: {
                    separator: 'top-[54px]',
                    item: 'gap-3'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: {
                    separator: 'top-[62px]',
                    item: 'gap-3.5'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

[SliderAn input to select a numeric value within a
range.](/components/slider)[SwitchA control that toggles between two
states.](/components/switch)

